from flask import render_template, request, Markup
from app.xss import xss_bp as bp


@bp.route('/')
def index():    
    return render_template('xss/index.html')

# @bp.route('/', methods=['POST'])
# def my_form_post():
#     # Simulate user-generated content
#     user_input = request.form['comment']
    
#     # Mitigate XSS by escaping user-generated content
#     # user_input = Markup.escape(user_input)

#     processed_text = user_input
    
#     return render_template('xss/index.html', user_input=f'<font color="purple">{processed_text}</font>')

@bp.route('/illegitimate', methods=['GET'])
def illegitimate():
    """
    All Inputs for reference:
    <font color="blue">Hello</font>
    Hello<style>body{background-color:pink;}
    """

    # Simulate user-generated content
    # user_input = request.form['comment']
    user_input = request.args.get('comment', '')

    processed_text = user_input
    
    return processed_text

@bp.route('/legitimate', methods=['GET'])
def legitimate():
    """
    All Inputs for reference:
    <font color="blue">Hello</font>
    Hello<style>body{background-color:pink;}
    """

    # Simulate user-generated content
    user_input = request.args.get('comment', '')
    
    # Mitigate XSS by escaping user-generated content
    user_input = Markup.escape(user_input)

    processed_text = user_input
    
    return processed_text

# @bp.route('/', methods=['POST'])
# def my_form_post():
#     # import pdb;pdb.set_trace()
#     text = request.form['text']
#     processed_text = text
#     return processed_text

# @bp.route('/user_profile')
# def user_profile():
#     # Simulate user-generated content
#     user_input = request.args.get('user_input', '')
    
#     # Mitigate XSS by escaping user-generated content
#     safe_user_input = Markup.escape(user_input)
    
#     return render_template('xss/index.html', user_input=safe_user_input)
