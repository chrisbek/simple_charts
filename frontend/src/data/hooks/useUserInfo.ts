import {useAtom, useSetAtom} from "jotai";
import {setUserInfoAtom, userInfoAtom} from "../atoms/userInfo";
import {UserInfo} from "../models/ShareChartData";


export const useUserInfo = (): [UserInfo | null, CallableFunction] => {
    const [userInfo] = useAtom(userInfoAtom);
    const setUserInfo = useSetAtom(setUserInfoAtom);

    return [userInfo, setUserInfo];
}