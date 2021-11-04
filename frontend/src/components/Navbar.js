import React from 'react'
import {Link} from 'react-router-dom'

function Navbar() {
    return (
        <nav>
            <div>
                <Link to="/page1">Page1</Link>
                <Link to ="/page2">Page2</Link>
            </div>
        </nav>
    )
}

export default Navbar
