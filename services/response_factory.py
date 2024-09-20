class ResponseFactory:
    def create_response(self, status, code, data, message):
        return {"status": status, "code": code, "data": data, "message": message}
