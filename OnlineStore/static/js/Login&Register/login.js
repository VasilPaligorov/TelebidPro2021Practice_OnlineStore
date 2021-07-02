class Login extends React.Component {
    constructor(props) {
        super(props);
        this.state = {

        }
    }

    render() {
        return (
            <>
                <div className="logo fadeInDown">
                    ТИТ-Тетимов
                </div>
                <div className="loginText fadeInDown">Log In</div>
                <div>
                    <label htmlFor="usr">Username or number:</label>
                    <input name="username" type="text" required/>
                </div>
                <div>
                    <label htmlFor="pwd">Password:</label>
                    <input name="password" type="password" required/>
                </div>
                <button type="submit" value="Submit">Submit</button>
                <br/>
                <p style="text-align: center; font-size: 20px;">You dont have a profile? <a
                    href="/register">Register</a>
                </p>
            </>
        )
    }
}