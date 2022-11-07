import { Chart } from "../components/Chart";
import { ChartPageLayout } from "../components/ChartPageLayout";
import { useSharedChartData } from "../data/hooks/useSharedChartData";
import {ErrorPage} from "./ErrorPage";

export const SharedChartPage = () => {
  const data = useSharedChartData();
  if (data == null) return <ErrorPage />;

  return <ChartPageLayout main={<Chart data={data} />} />;
};
