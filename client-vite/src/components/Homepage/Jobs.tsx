import { Link, useParams } from "react-router-dom";

const Jobs = () => {
  const { "*": routeParams } = useParams<{ "*": string }>();
  // const { companyName } = useParams<{ companyName: string }>();

  // Sample static job data for the selected company
  const jobs = [
    {
      id: 1,
      positionTitle: "Software Engineer",
      ctc: "80,000 - 100,000",
      location: "Bangalore",
      jobDescription: "Sample job description...",
      salaryRange: "80000-100000",
      duration: "Full Time",
      education: "Bachelor's Degree",
      skills: ["JavaScript", "React", "Node.js"],
      extraDetails: "Additional details about the job...",
      experience: "2-5 years",
      language: "English",
      locationDetail: "Bangalore, India",
    },
    {
      id: 2,
      positionTitle: "Frontend Developer",
      ctc: "70,000 - 90,000",
      location: "Mumbai",
      jobDescription: "Sample job description...",
      salaryRange: "70000-90000",
      duration: "Full Time",
      education: "Bachelor's Degree",
      skills: ["HTML", "CSS", "JavaScript"],
      extraDetails: "Additional details about the job...",
      experience: "3-7 years",
      language: "English",
      locationDetail: "Mumbai, India",
    },
    {
      id: 3,
      positionTitle: "Data Scientist",
      ctc: "90,000 - 120,000",
      location: "New York",
      jobDescription: "Sample job description...",
      salaryRange: "90000-120000",
      duration: "Full Time",
      education: "Master's Degree",
      skills: ["Python", "Machine Learning", "Data Analysis"],
      extraDetails: "Additional details about the job...",
      experience: "5-10 years",
      language: "English",
      locationDetail: "New York, USA",
    },
    // Add more job entries here
  ];
  if (!routeParams) {
    // Render all jobs
    return <h1 className="text-center text-3xl font-extrabold">All Jobs</h1>;
  } else {
    const params = routeParams.split("/");
    if (params.length === 1) {
      const [companyName] = params;
      // Render jobs for a specific company
      return (
        <div className="flex items-stretch h-screen p-10 bg-gray-50">
          {/* Filter Box */}
          <div className="w-1/4 p-4 border rounded-lg shadow-xl overflow-x-auto max-w-full bg-white">
            <h2 className="font-bold mb-2 text-center">All Filters</h2>
            <hr className="my-4 border-t-1 border-gray-300" />
            <ul className="space-y-4">
              {/* Company Type Filter */}
              <li className="m-4 pl-4 space-y-2">
                <h2 className="font-bold mb-2">Company Type</h2>
                <li>
                  <label className="flex items-center">
                    <input type="checkbox" className="mr-2" />
                    <span>Foreign MNC</span>
                    <span className="ml-1">(1149)</span>
                  </label>
                </li>
                <li>
                  <label className="flex items-center">
                    <input type="checkbox" className="mr-2" />
                    <span>Corporate</span>
                    <span className="ml-1">(681)</span>
                  </label>
                </li>
              </li>
              <hr className="my-4 border-t-1 border-gray-300" />
              {/* Location Filter */}
              <li className="m-4 pl-4 space-y-2">
                <h2 className="font-bold mb-2">Location</h2>
                <li>
                  <label className="flex items-center">
                    <input type="checkbox" className="mr-2" />
                    <span>Bangalore/Bengaluru</span>
                    <span className="ml-1">(1202)</span>
                  </label>
                </li>
                <li>
                  <label className="flex items-center">
                    <input type="checkbox" className="mr-2" />
                    <span>Delhi / NCR</span>
                    <span className="ml-1">(1088)</span>
                  </label>
                </li>
              </li>
              <hr className="my-4border-t-1 border-gray-300 " />
              {/* Industry Filter */}
              <li className="m-4 pl-4 space-y-2">
                <h2 className="font-bold mb-2">Industry</h2>
                <li>
                  <label className="flex items-center">
                    <input type="checkbox" className="mr-2" />
                    <span>IT Services & Consulting</span>
                    <span className="ml-1">(621)</span>
                  </label>
                </li>
                <li>
                  <label className="flex items-center">
                    <input type="checkbox" className="mr-2" />
                    <span>Software Product</span>
                    <span className="ml-1">(198)</span>
                  </label>
                </li>
              </li>
              <hr className="my-4 border-t-1 border-gray-300" />
              {/* Department Filter */}
              <li className="m-4 pl-4 space-y-2">
                <h2 className="font-bold mb-2">Department</h2>

                <li>
                  <label className="flex items-center">
                    <input type="checkbox" className="mr-2" />
                    <span>Engineering - Software & QA</span>
                    <span className="ml-1">(1418)</span>
                  </label>
                </li>
                <li>
                  <label className="flex items-center">
                    <input type="checkbox" className="mr-2" />
                    <span>Sales & Business Development</span>
                    <span className="ml-1">(1131)</span>
                  </label>
                </li>
                {/* Add other department filters here */}
              </li>
              <hr className="my-4 border-t-1 border-gray-300" />
              {/* Experience Filter */}
              <li className="m-4 pl-4 space-y-2">
                <h2 className="font-bold mb-2">Experience</h2>
                <li>
                  <label className="flex items-center">
                    <input type="checkbox" className="mr-2" />
                    <span>Experienced</span>
                    <span className="ml-1">(2417)</span>
                  </label>
                </li>
                <li>
                  <label className="flex items-center">
                    <input type="checkbox" className="mr-2" />
                    <span>Entry Level</span>
                    <span className="ml-1">(671)</span>
                  </label>
                </li>
              </li>
              <hr className="my-4 border-t-1 border-gray-300" />
              {/* Nature of Business Filter */}
              <li className="m-4 pl-4 space-y-2">
                <h2 className="font-bold mb-2">Nature of Business</h2>

                <li>
                  <label className="flex items-center">
                    <input type="checkbox" className="mr-2" />
                    <span>B2B</span>
                    <span className="ml-1">(1896)</span>
                  </label>
                </li>
                <li>
                  <label className="flex items-center">
                    <input type="checkbox" className="mr-2" />
                    <span>B2C</span>
                    <span className="ml-1">(981)</span>
                  </label>
                </li>
              </li>
              <hr className="my-4 border-t-1 border-gray-300" />
            </ul>
          </div>

          {/* Job Listings */}
          <div className="flex-grow p-4 w-3/4 ml-8">
            <h2 className="text-2xl font-bold mb-4">Jobs at {companyName}</h2>
            <div className="grid grid-cols-2 gap-4">
              {jobs.map((job) => (
                <div key={job.id} className="p-4 border rounded-lg bg-white">
                  <h3 className="text-lg font-semibold">{job.positionTitle}</h3>
                  <div className="mt-4 flex space-x-4">
                    <div className="flex items-center">
                      <span className="material-symbols-outlined mr-2">
                        currency_rupee
                      </span>
                      CTC
                      <div className="ml-2 px-4 rounded-xl bg-gray-100">
                        <p>{job.ctc}</p>
                      </div>
                    </div>
                    <div className="flex items-center">
                      <span className="material-symbols-outlined mr-2">
                        location_on
                      </span>
                      Location
                      <div className="ml-2 px-4 rounded-xl bg-gray-100">
                        <p>{job.location}</p>
                      </div>
                    </div>
                  </div>
                  <Link to={`/jobs/${companyName}/${job.id}`}>
                    <button className="bg-blue-500 text-white px-4 py-1.5 mt-8 rounded-xl float-right">
                      Apply Now
                    </button>
                  </Link>
                </div>
              ))}
            </div>
          </div>
        </div>
      );
    } else {
      // Invalid URL structure
      return <h2>Invalid URL</h2>;
    }
  }
};

export default Jobs;
