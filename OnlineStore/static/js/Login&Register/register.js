class Register extends React.Component {
    constructor(props) {
        super(props);
        this.state = {

        }
    }

    Register(){
        var server = "http://127.0.0.1:5000/"
        var username = document.register.username.value
        var number = document.register.number.value
        var email = document.register.email.value
        var password = document.register.password.value
        var repassword = document.register.repassword.value

        if (username && email && password && repassword) {
                $.ajax({
                    url: server + 'register',
                    type: 'POST',
                    data: {
                        "Username": username,
                        "Number": number,
                        "Email": email,
                        "Password": password,
                        "Repassword": repassword
                    }
                })
        }
    }

    render() {
        return (
             <>
                <div className="logo fadeInDown">
                    ТИТ-Тетимов
                </div>
                <div className="loginText fadeInDown">Register</div>
                <form name="register">
                    <div class="form-group">
                        <label htmlFor="username">Username:</label>
                        <input name="username" type="text" minlength="6" maxlength="16" required/>
                    </div>
                    <div class="form-group">
                        <label htmlFor="number">Number(Optional):</label>
                        <input type="number" name="number"/>
                        {/*<label id="error">{{message1}}</label>*/}
                    </div>
                    <div class="form-group">
                        <label htmlFor="email">Email:</label>
                        <input name="email" type="email" required/>
                        {/*<label id="error">{{message2}}</label>*/}
                    </div>
                    <div class="form-group">
                        <label htmlFor="password">Password:</label>
                        <input name="password" type="password" minlength="8" maxlength="8" size="8" required/>
                        {/*<label id="error">{{message3}}</label>*/}
                    </div>
                    <div class="form-group">
                        <label htmlFor="repassword">Re-Password:</label>
                        <input name="repassword" type="password" minlength="8" maxlength="8" size="8" required/>
                        {/*<label id="error">{{message3}}</label>*/}
                    </div>
                        <input type="submit" value="Submit" onClick={this.Register}/>
                </form>
                <br/>
                <p>Already have a profile? <a
                    href="/login">Sign in</a>
                </p>
            </>
        )
    }
}