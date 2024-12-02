from js import Response, Headers
import json

PATREON_DETAILS = {
    "name": "SourceBot",
    "url": "https://www.patreon.com/SourceBot"
}

DOMAIN = "http://cool-snow-b930.damaged-701.workers.dev"

PATH = "/video"

OPENGRAPH = """<!DOCTYPE html>
<html>
<head>
<meta charset=\"utf-8\">
<meta http-equiv="refresh" content="0;URL={url}">
<meta property=\"og:type\" content=\"video.other\">
<title></title>
<meta property="og:url" content="{url}">
<meta property="og:title" content=" ">
<meta property="og:site_name" content=" ">
<meta property="og:image" content="">
<meta property="og:video" content="{url}">
<meta property="og:description" content=" ">
<link rel="alternate" type="application/json+oembed" href="{domain}{path}/oembed.json?url={url}" title="Damaged">
</head>
<body>
<p>Redirecting you to <a href="{url}">{url}</a>. If you are not redirected in a few seconds, please click the link.</p>
</body>
</html>
<p>Served From Cloudflare</p>
"""

def add_content_type(input: str, content_type: str) -> str:
    return input.replace("</head>", f"<meta property=\"og:video:type\" content=\"video/{content_type}\">\n</head>", 1)

def format_HTML(input: str, url: str) -> str:
    return input.format(url=url, domain=DOMAIN, path=PATH)

def on_fetch(request):
    target_url: str = request.url.split("=", 1)[1].replace("\"", "&quot;")
    path_url: str = request.url.split("?", 1)[0]
    if "oembed" in path_url:
        data: Response = do_oembed(target_url)
    else:
        data: Response = do_opengraph(target_url, path_url)
    return data

def do_oembed(url: str) -> Response:
    headers = Headers.new({"content-type": "application/json"}.items())
    data = json.dumps({
        "version": "1.0",
        "type": "rich",
        "title": " ",
        "author_name": "Video Link",
        "author_url": url,
        "provider_name": PATREON_DETAILS["name"],
        "provider_url": PATREON_DETAILS["url"],
        "url": url
    })
    return Response.new(data, headers=headers)

def do_opengraph(url, path_url):
    format = path_url.rsplit("/", 1)[1]
    if format != "video":
        html = add_content_type(OPENGRAPH, format)
    else:
        html = OPENGRAPH
    headers = Headers.new({"content-type": "text/html;charset=UTF-8"}.items())
    return Response.new(format_HTML(html, url), headers=headers)
