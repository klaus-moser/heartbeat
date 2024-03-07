#!/usr/bin/env python3

# Filename: http_heartbeat_flask.py

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


""" HTTP-Heartbeat via Flask. """

import os
from flask import Flask
from time import ctime

__version__ = "0.1"
__author__ = "klaus-moser"
__date__ = ctime(os.path.getmtime(__file__))

# Create & Initialize Flask app
app = Flask(__name__)


@app.route('/health')
def health_check():
    # TODO: further checks
    return "ok", 200


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
