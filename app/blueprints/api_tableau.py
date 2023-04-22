from flask import Blueprint, jsonify, make_response
import requests



tableau_bp = Blueprint("tableau",__name__)



@tableau_bp("api/v1_tableau/all")
def retorna_app():
    return 
def retorna_login_admin_tableau():
    def sig_in_ad_admin():
        url = "https://{{server}}/api/{{api-version}}/auth/signin"

        payload = "<tsRequest>\n    <credentials name=\"{{admin-username}}\" password=\"{{admin-password}}\">\n        <site contentUrl=\"{{content-url}}\"/>\n    </credentials>\n</tsRequest>"
        headers = {
        'Content-Type': 'application/xml'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        return 
    
    return 