import {useAtom, useSetAtom} from "jotai";
import {useEffect} from "react";
import {
  fetchSharedChartDataAtom,
  setSharedChartDataLoadingStartedAtom,
  sharedChartDataAtom,
  sharedChartDataLoadingStartedAtom,
} from "../atoms/sharedChartData";
import {useUserInfo} from "./useUserInfo";

export const useSharedChartData = () => {
  const [userInfo] = useUserInfo()
  const [chartData] = useAtom(sharedChartDataAtom);
  const fetchChartData = useSetAtom(fetchSharedChartDataAtom);

  useEffect(() => {
    fetchChartData(userInfo);
  }, [fetchChartData]);

  return chartData;
};

export const useSharedChartDataLoading = (): [boolean, CallableFunction] => {
  const [sharedChartDataLoadingStarted] = useAtom(sharedChartDataLoadingStartedAtom)
  const setSharedChartDataLoadingStarted = useSetAtom(setSharedChartDataLoadingStartedAtom)

  return [sharedChartDataLoadingStarted, setSharedChartDataLoadingStarted]
}