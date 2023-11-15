import typing
from os import PathLike
from typing import Annotated, Optional, Mapping, cast

from fastapi import Depends, Request
from starlette.background import BackgroundTask
from starlette.templating import Jinja2Templates, _TemplateResponse  # noqa

from config import TEMPLATES_DIR
from ui.flows import CommonUIData


class HtmxAwareTemplates(Jinja2Templates):
    common_ui_data: dict

    def __init__(
        self,
        directory: typing.Union[str, PathLike],
        common_ui_data: dict,
        context_processors: typing.Optional[
            typing.List[typing.Callable[[Request], typing.Dict[str, typing.Any]]]
        ] = None,
        **env_options: typing.Any
    ) -> None:
        self.common_ui_data = common_ui_data
        super().__init__(directory, context_processors, **env_options)

    def HtmxAwareTemplateResponse(  # noqa
        self,
        name: str,
        context: dict,
        status_code: int = 200,
        headers: Optional[Mapping[str, str]] = None,
        media_type: Optional[str] = None,
        background: Optional[BackgroundTask] = None,
    ) -> _TemplateResponse:
        if "request" not in context:
            raise ValueError('context must include a "request" key')

        request = cast(Request, context["request"])

        if request.headers.get("HX-Request") != "true":
            context.update({"template_path": name})
            context["collections"] = self.common_ui_data["collections"]
            name = "partial_to_full.html"

        return self.TemplateResponse(
            name, context, status_code, headers, media_type, background
        )


def get_templates(common_ui_data: CommonUIData) -> HtmxAwareTemplates:
    return HtmxAwareTemplates(directory=TEMPLATES_DIR, common_ui_data=common_ui_data)


Templates = Annotated[HtmxAwareTemplates, Depends(get_templates)]
