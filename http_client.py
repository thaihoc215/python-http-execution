import httpx
import uuid


async def async_request(
    url: str,
    method: str = "GET",
    params: dict = None,
    headers: dict = None,
    body: object = None,
    follow_redirects: bool = True,
    content_type: str = None,
    files: dict = None,
):
    try:
        async with httpx.AsyncClient(follow_redirects=follow_redirects, timeout=60.0) as client:
            method = method.upper()
            if method == "POST":
                response = await client.post(
                    url,
                    params=params,
                    headers=headers,
                    files=files,
                    data=body if content_type == "form" else None,
                    content=body if content_type == "raw" else None,
                    timeout=60.0
                )
            elif method == "GET":
                response = await client.get(url, params=params, headers=headers, timeout=60.0)
            elif method == "PUT":
                if content_type == "json":
                    response = await client.put(
                        url, params=params, headers=headers, json=body, timeout=60.0
                    )
                elif content_type == "form":
                    response = await client.put(
                        url, params=params, headers=headers, data=body, timeout=60.0
                    )
                elif content_type == "raw":
                    response = await client.put(
                        url, params=params, headers=headers, content=body, timeout=60.0
                    )
                else:
                    if isinstance(body, dict):
                        response = await client.put(
                            url, params=params, headers=headers, json=body, timeout=60.0
                        )
                    elif body is not None:
                        response = await client.put(
                            url, params=params, headers=headers, content=body, timeout=60.0
                        )
                    else:
                        response = await client.put(url, params=params, headers=headers, timeout=60.0)
            elif method == "DELETE":
                response = await client.delete(url, params=params, headers=headers, timeout=60.0)
            else:
                raise ValueError(f"Unsupported HTTP method: {method}")
            print(f"[{method}] Status: {response.status_code}, Body: {response.text[:500]}\n\n")
            response.raise_for_status()
    except httpx.HTTPStatusError as exc:
        print(f"HTTP error occurred: {exc.response.status_code} - {exc.response.text}\n")
        raise
    except Exception as exc:
        print(f"An unexpected error occurred: {exc}\n")
        raise