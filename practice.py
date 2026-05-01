class libarayitem:
    def __init__(self, title ,creator):
        self.title = title
        self.creator = creator
        self._is_checked_out = False

    def display_info(self):
        status = "checked out " if self._is_checked_out else "available"
        return f"'{self.title}' by {self.creator} - [{status}]"
    