import {useAtom, useSetAtom} from "jotai";
import {useEffect} from "react";
import {fetchSharingTokenAtom, sharingTokenLoadingAtom} from "../atoms/sharingToken";
import {UserInfo} from "../models/ShareChartData";
import {useSharingTokenLoadingRequested} from "./useSharingLink";
import {useUserInfo} from "./useUserInfo";

export const useFetchSharingLink = (): boolean => {
    const fetchToken = useSetAtom(fetchSharingTokenAtom);
    const [sharingTokenLoadingRequested,] = useSharingTokenLoadingRequested();
    const [userInfo,] = useUserInfo();
    const [sharingTokenLoading,] = useAtom(sharingTokenLoadingAtom);

    useEffect(() => {
        if (!sharingTokenLoadingRequested) return
        if (sharingTokenLoading) return;

        if (userInfo instanceof UserInfo) {
            fetchToken(userInfo)
        }
    }, [sharingTokenLoadingRequested]);

    return sharingTokenLoading;
};
