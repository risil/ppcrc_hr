import { BrowserRouter, Route, Routes } from "react-router-dom";
import HomePage from "./components/Homepage/HomePage";
// import Login from "./components/Login/Login";
import Login1 from "./components/Login/Login1";
import Navbar from "./components/Navbar/Navbar";
import Register2 from "./components/Register/Register2";
import Jobs from "./components/Homepage/Jobs";
import Companies from "./components/Homepage/Companies";
import UploadResume from "./components/UploadResume";
import JobDescription from "./components/JobDescription/JobDescription";
import EmployerLogin from "./components/Login/EmployerLogin";
import JobDetails from "./components/Homepage/JobDetails";
// import Register1 from "./components/Register/Register1";
import EmployeeRegister from "./components/Register/EmployeeRegister";

function App() {
  return (
    <BrowserRouter>
      <div className="App">
        <Navbar />
        {/* <HomePage /> */}
        <Routes>
          {/* <Route path="/userlogin" element={<Login />} /> */}
          <Route path="/userlogin" element={<Login1 />} />
          <Route path="/employerlogin" element={<EmployerLogin />} />
          <Route path="/jobdescription" element={<JobDescription />} />
          <Route path="/jobdetails" element={<JobDetails />} />
          <Route path="/employerregistration" element={<EmployeeRegister />} />
          <Route path="/" element={<HomePage />} />
          <Route path="/userregister" element={<Register2 />} />
          <Route path="/jobs" element={<Jobs />} />
          <Route path="/jobs/*" element={<Jobs />} />
          <Route path="/jobs/:companyName/:jobId" element={<JobDetails />} />

          <Route path="/companies" element={<Companies />} />
          <Route path="/uploadresume" element={<UploadResume />} />

          {/* <Route path="/api/login" element={<Login />} />
          <Route path="/api/register" element={<Register />} /> */}
        </Routes>
      </div>
    </BrowserRouter>
  );
}

export default App;
