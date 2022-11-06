from factory import create_app
app = create_app('prod')
if __name__ == "__main__":
    app.run()