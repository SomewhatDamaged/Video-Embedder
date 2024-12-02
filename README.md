Factored as a Cloudflare Python Worker.

Responds to a given video URL such that Discord/et;al can embed it.

Output is (depending on endpoint; you can force a video mime type):


https://excessive.space/video/mp4?url=https://bsky.social/xrpc/com.atproto.sync.getBlob?did=did:plc:7uczurhtoruazft4367p2yi7&cid=bafkreidg4h5qdeu4vpptbkb6tz3ft6wnar27ziwnx3skk6bwtkhkpejcba
```html
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<meta http-equiv="refresh" content="0;URL=https://bsky.social/xrpc/com.atproto.sync.getBlob?did=did:plc:7uczurhtoruazft4367p2yi7&cid=bafkreidg4h5qdeu4vpptbkb6tz3ft6wnar27ziwnx3skk6bwtkhkpejcba">
<meta property="og:type" content="video.other">
<title></title>
<meta property="og:url" content="https://bsky.social/xrpc/com.atproto.sync.getBlob?did=did:plc:7uczurhtoruazft4367p2yi7&cid=bafkreidg4h5qdeu4vpptbkb6tz3ft6wnar27ziwnx3skk6bwtkhkpejcba">
<meta property="og:title" content=" ">
<meta property="og:site_name" content=" ">
<meta property="og:image" content="">
<meta property="og:video" content="https://bsky.social/xrpc/com.atproto.sync.getBlob?did=did:plc:7uczurhtoruazft4367p2yi7&cid=bafkreidg4h5qdeu4vpptbkb6tz3ft6wnar27ziwnx3skk6bwtkhkpejcba">
<meta property="og:description" content=" ">
<link rel="alternate" type="application/json+oembed" href="http://excessive.space/video/oembed.json?url=https://bsky.social/xrpc/com.atproto.sync.getBlob?did=did:plc:7uczurhtoruazft4367p2yi7&cid=bafkreidg4h5qdeu4vpptbkb6tz3ft6wnar27ziwnx3skk6bwtkhkpejcba" title="Damaged">
<meta property="og:video:type" content="video/mp4">
</head>
<body>
<p>Redirecting you to <a href="https://bsky.social/xrpc/com.atproto.sync.getBlob?did=did:plc:7uczurhtoruazft4367p2yi7&cid=bafkreidg4h5qdeu4vpptbkb6tz3ft6wnar27ziwnx3skk6bwtkhkpejcba">https://bsky.social/xrpc/com.atproto.sync.getBlob?did=did:plc:7uczurhtoruazft4367p2yi7&cid=bafkreidg4h5qdeu4vpptbkb6tz3ft6wnar27ziwnx3skk6bwtkhkpejcba</a>. If you are not redirected in a few seconds, please click the link.</p>
<p>Served From Cloudflare</p>
</body>
</html>
```

http://excessive.space/video/oembed.json?url=https://bsky.social/xrpc/com.atproto.sync.getBlob?did=did:plc:7uczurhtoruazft4367p2yi7&cid=bafkreidg4h5qdeu4vpptbkb6tz3ft6wnar27ziwnx3skk6bwtkhkpejcba
```json
{
    "version": "1.0",
    "type": "rich",
    "title": " ",
    "author_name": "Video Link",
    "author_url": "https://bsky.social/xrpc/com.atproto.sync.getBlob?did=did:plc:7uczurhtoruazft4367p2yi7&cid=bafkreidg4h5qdeu4vpptbkb6tz3ft6wnar27ziwnx3skk6bwtkhkpejcba",
    "provider_name": "SourceBot",
    "provider_url": "https://www.patreon.com/SourceBot",
    "url": "https://bsky.social/xrpc/com.atproto.sync.getBlob?did=did:plc:7uczurhtoruazft4367p2yi7&cid=bafkreidg4h5qdeu4vpptbkb6tz3ft6wnar27ziwnx3skk6bwtkhkpejcba"
}
```
