from flask import Flask, render_template, request, redirect, url_for, session
# from flaskext.mysql import MySQL

app = Flask(__name__)

# generated using `python -c "import secrets; print(secrets.token_hex())"`
app.secret_key = 'ce0fe1f5bfc12f9cbd568312b5de3ac82eb6f5457c2b272d49456be8f7d5dc82'

# home
@app.route('/')
def home():
    return render_template('home.html')

# login
@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    
    if request.method == 'POST':
        session['user_type']=1
        session['full_name']='Akshay Ramesh'
        return redirect(url_for('churn_list',level='high'))

@app.route('/logout')
def logout():
    return redirect(url_for('login'))

# churn
@app.route('/churn/<level>')
def churn_list(level):
    rows = []
    if level == 'high':
        rows = [
            {
                'customer_id': '1111',
                'full_name': 'Akshay Ramesh P',
                'phone': '9847111111',
                'churn':'80',
                'last_call': '2023-11-01 17:03:00'
            },
            {
                'customer_id': '1112',
                'full_name': 'Vinaya B R',
                'phone': '9847222222',
                'churn':'70',
                'last_call': 'No Response'
            },
        ]
    elif level == 'medium':
         rows = [
            {
                'customer_id': '1113',
                'full_name': 'Akshay Dath MV',
                'phone': '9847333333',
                'churn':'60',
                'last_call': '2023-11-04 15:50:00'
            }
        ]
    elif level == 'low':
        rows = [
            {
                'customer_id': '1114',
                'full_name': 'Sanusha AK',
                'phone': '9847444444',
                'churn':'30',
                'last_call': '2023-11-05 10:22:00'
            }
        ]
    
    return render_template('churn.html',rows=rows)

# user list 
@app.route("/user")
def user_list():
    rows = [
            {
                'user_id': '2111',
                'user_type': 1,
                'full_name': 'Akshay Ramesh P',
                'id_card_number': '515352'
            },
            {
                'user_id': '2112',
                'user_type': 2,
                'full_name': 'Vinaya B R',
                'id_card_number': '1425232'
            },
            {
                'user_id': '2113',
                'user_type': 3,
                'full_name': 'Akshay Dath MV',
                'id_card_number': '23615253'
            },
            {
                'user_id': '2114',
                'user_type': 3,
                'full_name': 'Sanusha AK',
                'id_card_number': '3462532'
            }
            ]    
    return render_template("user-list.html",rows=rows)

# user new
@app.route('/user/new',methods=['GET','POST'])
def user_new():
    if request.method == 'GET':
        return render_template("user-new.html")
    
    if request.method == 'POST':
        return redirect(url_for('user_list'))
    
# user view
@app.route('/user/view/<user_id>',methods=['GET'])
def user_view(user_id):
    if request.method == 'GET':
        return render_template("user-view.html")

# user edit
@app.route('/user/edit/<user_id>',methods=['GET','POST'])
def user_edit(user_id):
    if request.method == 'GET':
        return render_template("user-edit.html")
    
    if request.method == 'POST':
        return redirect(url_for('user_list'))

# user password reset
@app.route('/user/password-reset/<user_id>',methods=['GET','POST'])
def user_password_reset(user_id):
    if request.method == 'GET':
        return render_template("confirm.html",title='Confirm Password Reset',msg='Do you want to reset password?',cancel_redirect=url_for('user_list'))
    
    if request.method == 'POST':
        return redirect(url_for('user_list'))

# user remove
@app.route('/user/remove/<user_id>',methods=['GET','POST'])
def user_remove(user_id):
    if request.method == 'GET':
        return render_template("confirm.html",title='Confirm User Removal',msg='Do you want to remove user?',cancel_redirect=url_for('user_list'))
    
    if request.method == 'POST':
        return redirect(url_for('user_list'))

# customer list 
@app.route("/customer")
def customer_list():
    rows = [
            {
                'customer_id': '1111',
                'full_name': 'Akshay Ramesh P',
                'phone': '9847111111'
            },
            {
                'customer_id': '1112',
                'full_name': 'Vinaya B R',
                'phone': '9847222222'
            },
            {
                'customer_id': '1113',
                'full_name': 'Akshay Dath MV',
                'phone': '9847333333'
            },
            {
                'customer_id': '1114',
                'full_name': 'Sanusha AK',
                'phone': '9847444444'
            }
            ]    
    return render_template('customer-list.html',rows=rows)

# customer new
@app.route('/customer/new',methods=['GET','POST'])
def customer_new():
    if request.method == 'GET':
        return render_template("customer-new.html")
    
    if request.method == 'POST':
        return redirect(url_for('customer_list'))
    
# customer view
@app.route('/customer/view/<customer_id>',methods=['GET'])
def customer_view(customer_id):
    if request.method == 'GET':
        return render_template("customer-view.html")

# customer edit
@app.route('/customer/edit/<customer_id>',methods=['GET','POST'])
def customer_edit(customer_id):
    if request.method == 'GET':
        return render_template("customer-edit.html")
    
    if request.method == 'POST':
        return redirect(url_for('customer_list'))

# customer remove
@app.route('/customer/remove/<customer_id>',methods=['GET','POST'])
def customer_remove(customer_id):
    if request.method == 'GET':
        return render_template("confirm.html",title='Confirm Customer Data Removal',msg='Do you want to remove customer data?',cancel_redirect=url_for('customer_list'))
    
    if request.method == 'POST':
        return redirect(url_for('customer_list'))
    
# customer mark call
@app.route('/customer/markcall/<customer_id>',methods=['POST'])
def customer_markcall(customer_id):  
    if request.method == 'POST':
        return redirect(url_for('churn_list',level='high'))


if __name__ == "__main__":
    app.run(debug=True)