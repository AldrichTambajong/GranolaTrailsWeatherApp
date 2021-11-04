import React from 'react'
import {Link} from 'react-router-dom'

function Navbar() {
    return (
        <nav className="navbar">
            <div className="container-fluid">
                <ul className= "header-nav">
                    <li><Link className ="link" to="/home">Home</Link></li>
                    <li><Link className="link"to ="">Page2</Link></li>
                </ul>
            </div>
        </nav>
        
    )
}

export default Navbar
