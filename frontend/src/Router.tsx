import {ChartPage} from "./pages/ChartPage";
import {UserCredentialsPage} from "./pages/UserCredentialsPage";

export const Router = () => {
  const page = window.location.pathname;

  if (page.startsWith("/share/chart")) return <UserCredentialsPage/>;

  else return <ChartPage/>;
};
