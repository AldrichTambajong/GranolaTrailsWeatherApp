import React from "react";
import { useEffect } from "react";
import { Navigate } from "react-router-dom";
function Logout(props) {
  const { setLoggedIn } = props;
  function handleLogout() {
    console.log("logging out");
    sessionStorage.clear();
    localStorage.clear();
    setLoggedIn(false);
  }

  useEffect(() => {
    handleLogout();
  });

  return <Navigate to='/login'></Navigate>;
}

export default Logout;
