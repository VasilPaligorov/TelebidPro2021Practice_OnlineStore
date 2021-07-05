class Login extends React.Component {
    constructor(props) {
        super(props);
        this.state = {

        }
    }

    Login(){
        var server = "http://127.0.0.1:5000/"
        var username = document.login.username.value
        var password = document.login.password.value

        if (username && password){
            if (username && password) {
                $.ajax({
                    url: server + 'login',
                    type: 'POST',
                    data: {"Username": username, "Password": password}
                })
            }
        }
    }

    render() {
        return (
            <>
                <div className="logo fadeInDown">
                    ТИТ-Тетимов
                </div>
                <div className="loginText fadeInDown">Log In</div>
                <form name="login" id="logi">
                    <div class="form-group">
                        <label htmlFor="usr">Username or number:</label>
                        <input name="username" type="text" required/>
                    </div>

                    <div class="form-group">
                        <label htmlFor="pwd">Password:</label>
                        <input name="password" type="password" minlength="8" maxlength="8" size="8" required/>
                        {/*<label id="error">{{message}}</label>*/}
                    </div>
                    <input class="form-group" type="submit" value="Submit" onClick={this.Login}/>
                </form>
                <br/>
                <p>You dont have a profile? <a
                    href="/register">Register</a>
                </p>
            </>
        )
    }
}