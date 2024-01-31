import typing
from collections.abc import Mapping
from os import PathLike
from typing import Annotated, cast

from fastapi import Depends, Request
from starlette.background import BackgroundTask
from starlette.templating import Jinja2Templates, _TemplateResponse  # noqa

from src.config import TEMPLATES_DIR
from src.ui.flows import CommonUIData


class HtmxAwareTemplates(Jinja2Templates):
    common_ui_data: dict

    def __init__(
        self,
        directory: str | PathLike,
        common_ui_data: dict,
        context_processors: list[typing.Callable[[Request], dict[str, typing.Any]]]
        | None = None,
        **env_options: typing.Any,
    ) -> None:
        self.common_ui_data = common_ui_data
        super().__init__(directory, context_processors, **env_options)

    def HtmxAwareTemplateResponse(  # noqa
        self,
        name: str,
        context: dict,
        status_code: int = 200,
        headers: Mapping[str, str] | None = None,
        media_type: str | None = None,
        background: BackgroundTask | None = None,
    ) -> _TemplateResponse:
        if "request" not in context:
            raise ValueError('context must include a "request" key')

        request = cast(Request, context["request"])

        if request.headers.get("HX-Request") != "true":
            context.update({"template_path": name, **self.common_ui_data})
            name = "partial_to_full.html"

        return self.TemplateResponse(
            name, context, status_code, headers, media_type, background
        )


def get_templates(common_ui_data: CommonUIData) -> HtmxAwareTemplates:
    return HtmxAwareTemplates(directory=TEMPLATES_DIR, common_ui_data=common_ui_data)


Templates = Annotated[HtmxAwareTemplates, Depends(get_templates)]
