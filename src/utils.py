from flask import request


def inspect_request():
    return {
        "ip": request.remote_addr,
        "method": request.method,
        "url": request.url,
        "path": request.path,
        "headers": dict(request.headers),
        "query_parameters": request.args.to_dict(),
        "form_data": request.form.to_dict()
    }