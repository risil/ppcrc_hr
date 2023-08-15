import { useParams } from "react-router-dom";

const Jobs = () => {
  const { "*": routeParams } = useParams<{ "*": string }>();

  if (!routeParams) {
    // Render all jobs
    return <h1 className="text-center text-3xl font-extrabold">All Jobs</h1>;
  } else {
    const params = routeParams.split("/");
    if (params.length === 1) {
      const [companyName] = params;
      // Render jobs for a specific company
      return (
        <h1 className="text-center text-3xl font-extrabold">
          Jobs by {companyName}
        </h1>
      );
    } else if (params.length === 2) {
      const [companyName, designation] = params;
      // Render jobs for a specific company and designation
      return (
        <h1 className="text-center text-3xl font-extrabold">
          Jobs for {companyName} - {designation}
        </h1>
      );
    } else {
      // Invalid URL structure
      return <h2>Invalid URL</h2>;
    }
  }
};

export default Jobs;
