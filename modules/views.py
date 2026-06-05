import markdown
from markdown.extensions.codehilite import CodeHiliteExtension
from markdown.extensions.fenced_code import FencedCodeExtension
from markdown.extensions.tables import TableExtension
from markdown.extensions.toc import TocExtension
from django.shortcuts import render, get_object_or_404
from django.utils.safestring import mark_safe
from .models import Module


def module_detail(request, slug):
    """
    Immersive module lesson page with:
    - Server-side markdown rendering (with syntax highlighting, TOC, fenced code)
    - Course sibling modules for the left-sidebar navigation tree
    - Prev/next module navigation
    """
    module = get_object_or_404(Module, slug=slug)
    course = module.course
    all_modules = list(course.modules.all())

    # ── Markdown rendering ─────────────────────────────────────────────────
    md = markdown.Markdown(
        extensions=[
            FencedCodeExtension(),
            CodeHiliteExtension(
                css_class='highlight',
                linenums=False,
                guess_lang=True,
            ),
            TableExtension(),
            TocExtension(
                toc_depth='2-4',
                anchorlink=True,
                title='',
            ),
            'markdown.extensions.admonition',
            'markdown.extensions.attr_list',
            'markdown.extensions.def_list',
            'markdown.extensions.abbr',
        ]
    )

    rendered_content = mark_safe(md.convert(module.markdown_content or ''))
    toc = mark_safe(md.toc)               # HTML TOC built by TocExtension

    # ── Prev / Next ────────────────────────────────────────────────────────
    current_index = next(
        (i for i, m in enumerate(all_modules) if m.pk == module.pk), None
    )
    prev_module = all_modules[current_index - 1] if current_index and current_index > 0 else None
    next_module = all_modules[current_index + 1] if current_index is not None and current_index < len(all_modules) - 1 else None

    context = {
        'module': module,
        'course': course,
        'all_modules': all_modules,
        'rendered_content': rendered_content,
        'toc': toc,
        'prev_module': prev_module,
        'next_module': next_module,
        'current_index': current_index,
        'total_modules': len(all_modules),
    }
    return render(request, 'modules/detail.html', context)
