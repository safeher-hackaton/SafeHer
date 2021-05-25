import './header.css';

function Header() {
    return (
        <div className="app-header">
            <div>
                <img src={process.env.PUBLIC_URL + '/safeher-logo.png'} />
            </div>
            <div></div>
            <div className="header-left">הרשמה | התחברות</div>
        </div>
    )
}

export default Header;
