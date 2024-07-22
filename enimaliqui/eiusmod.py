class View:
    def display(self, data):
        print(f"View: Displaying {data}")

class ViewProxy:
    def __init__(self, view):
        self._view = view
        self._modified_view = None

    def modify_view(self, new_data):
        self._modified_view = f"Modified {new_data}"

    def display(self):
        if self._modified_view:
            self._view.display(self._modified_view)
        else:
            self._view.display("Default Data")

# Client code
view = View()
view_proxy = ViewProxy(view)

# Modifying and displaying the view through the proxy
view_proxy.modify_view("Data")
view_proxy.display()  # Output: View: Displaying Modified Data
