from flask import Flask, render_template, request, session
from settings import VERSION, APPLICATION_SECRET_KEY
from captcha import generate_captcha
import json
from uuid import uuid4
import smtplib
from email.message import EmailMessage

application = Flask(__name__)
application.secret_key = APPLICATION_SECRET_KEY



@application.route('/')
def index():
    """

    :return:
    """
    return render_template('index.html', version=VERSION)

@application.route('/pricing')
def pricing():
    """

    :return:
    """

    return render_template('pricing.html', version=VERSION)

@application.route('/contact')
def contact():
    """

    :return:
    """

    return render_template('contact.html', version=VERSION)


@application.route('/rnotes')
def release_notes():
    """

    :return:
    """
    return render_template('release_notes.html', version=VERSION)

"""

"""
@application.route('/schedule')
def schedule():
    """
    :return:
    """

    # start with a clean form id by removing any previous ones
    removeSessionValue('formId-request')

    #BIM-Simple-Captcha
    if(request.args.get('session') == 'clear'):
        removeSessionValue('captcha')
    # store in the session the right answer
    challengeQuestion, challengeSolution, challengeStrings = generate_captcha()

    # generate an ID, set it in the session, and pass it as a hidden form param.  Verify it upon form submission
    formId = setFormId()


    return render_template('schedule.html', version=VERSION, cq=challengeQuestion, cs=challengeSolution, co=challengeStrings, sessionCaptcha=getSessionValue('captcha'), formId=formId)


def generateUniqueId():
    return str(uuid4()).replace("'", "")

def setFormId():
    id = generateUniqueId()
    setSessionValue('formId-request', id)
    return id


"""
SESSION HANDLERS
"""
def getSessionValue(valueName):
    if valueName in session.keys():
        return session[valueName]
    return None

def removeSessionValue(valueName):
    if valueName in session.keys():
        session.pop(valueName)
    return True

def setSessionValue(valueName, value):
    session[valueName] = value
    return True


"""

"""
@application.route('/ajax_captcha')
def ajax_capcha():
    # store a success session value for the browser/user session
    setSessionValue('captcha', True)
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'}

"""

"""
@application.route('/scheduleFormSubmit', methods=['POST'])
def processRequestForm():
    company = request.form['requesting_entity']
    fullName = request.form['contact_first_last']
    phone = request.form['contact_phone']
    email = request.form['contact_email']
    desc = request.form['request_desc']
    formId = request.form['formId']

    if formId == getSessionValue('formId-request'):

        #mail only if company or full name are present, and phone or email, and short desc
        if (company or fullName) and (phone or email) and desc:
            msg = EmailMessage()
            msg.set_content("Company: %s, full name: %s, phone: %s, email: %s, desc: %s, formId: %s" % (company, fullName, phone, email, desc, formId) )
            msg['Subject'] = "Bad Idea Metals Request Form - %s" % (formId)
            msg['From'] = 'no-reply@badideametals.com'
            msg['To'] = 'badideametals@gmail.com'
            s = smtplib.SMTP('localhost')
            s.send_message(msg)
            s.quit()
            return render_template('scheduleFormThankYou.html', version=VERSION)
        else:
            return render_template('scheduleFormThankYouError.html', version=VERSION)

    else:
        # make form expired
        return render_template('scheduleFormThankYouFormExpired.html', version=VERSION)

if __name__ == '__main__':
    application.run(host="0.0.0.0", port=80)

