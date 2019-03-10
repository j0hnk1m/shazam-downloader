from flask import Flask, render_template, send_from_directory
import main
import getpass
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('ui.html')


@app.route('/download', methods=['POST'])
def foo():
	main.main()
	return send_from_directory('/Users/' + getpass.getuser() + '/Downloads', 'client_ss_downloads.zip')


if __name__ == '__main__':
	app.run()
