import React from "react";
import { Link } from "react-router-dom";

function Navbar() {
  return (
    <nav class="navbar navbar-expand-lg justify-content-between">
      <a class="navbar-brand mb-0 h1">Granola Trails</a>

      <div class="collapse navbar-collapse me-auto" id="navbarSupportedContent">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
        </ul>
        <Link className="nav-link" to='/home'>Home</Link>
        <Link className='nav-link' to='/logout'>Logout</Link>
      </div>
    </nav>
  );
}

export default Navbar;
