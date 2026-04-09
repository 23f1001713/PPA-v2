from flask import jsonify

def success_response(data=None, message="Success", status_code=200):
    """Generate success response"""
    response = {
        "success": True,
        "message": message,
        "data": data if data is not None else {}
    }
    return jsonify(response), status_code

def error_response(message="Error", errors=None, status_code=400):
    """Generate error response"""
    response = {
        "success": False,
        "message": message,
        "errors": errors if errors else []
    }
    return jsonify(response), status_code

def paginated_response(items, total, page, per_page, message="Success"):
    """Generate paginated response"""
    response = {
        "success": True,
        "message": message,
        "data": {
            "items": items,
            "pagination": {
                "total": total,
                "page": page,
                "per_page": per_page,
                "total_pages": (total + per_page - 1) // per_page
            }
        }
    }
    return jsonify(response), 200