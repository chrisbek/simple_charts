import {atom} from "jotai";
import {fetchSharedChartData} from "../../api/sharing";
import {getShareTokenFromUrl} from "../../utils/getShareTokenFromUrl";
import {ChartData} from "../models/ChartData";
import {UserInfo} from "../models/ShareChartData";

export const sharedChartDataAtom = atom<ChartData | null>(null);
export const sharedChartDataLoadingAtom = atom(true);
export const sharedChartDataLoadingStartedAtom = atom(false);
export const sharedChartDataErrorAtom = atom<string | null>(null);
export const fetchSharedChartDataAtom = atom(null, async (_, set, userInfo: UserInfo | null) => {
    const token = getShareTokenFromUrl();
    set(sharedChartDataErrorAtom, null);

    try {
        if (userInfo?.email != null) {
            const chartData = await fetchSharedChartData(token, userInfo.email);
            set(sharedChartDataAtom, chartData);
        }
    } catch (error: any) {
        set(sharedChartDataErrorAtom, error.message);
    }
    set(sharedChartDataLoadingAtom, false);
});


export const setSharedChartDataLoadingStartedAtom = atom(null, async (_, set, value: boolean) => {
    set(sharedChartDataLoadingStartedAtom, value);
});