// import React from "react";

import { Link } from "react-router-dom";

const Navbar = () => {

  return (
    <div className="navBar flex justify-between items-center p-[2rem] sticky">
      <div className="logoDiv flex gap-10 items-center">
        <Link to="/">
          <h1 className="logo text-2xl text-blueColor">
            <strong className="tracking-wide">RESULT</strong>
          </h1>
        </Link>
        {/* <li className="menuList text-[#6f6f6f] hover:text-blueColor">Jobs</li>
        <li className="menuList text-[#6f6f6f] hover:text-blueColor">
          Companies
        </li> */}
      </div>
      <div className="menu flex items-center gap-8">
        <Link to="/jobs">
          <li className="menuList text-[#6f6f6f] hover:text-blueColor">Jobs</li>
        </Link>
        <Link to="/companies">
          <li className="menuList text-[#6f6f6f] hover:text-blueColor">
            Companies
          </li>
        </Link>

        <Link to="/login">
          <button className="loginBtn ">Login</button>
        </Link>
        <Link to="/register">
          <button className="registerBtn">Register</button>
        </Link>

        <div className="h-8 w-0.5 bg-gray-400"></div>
        <li className="menuList text-[#6f6f6f] hover:text-blueColor">
          Employers
        </li>
      </div>
    </div>
  );
};

export default Navbar;
