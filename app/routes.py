from app import wave_finder_app

@wave_finder_app.route('/')
@wave_finder_app.route('/index')
def index():
    return "Hello, World!"