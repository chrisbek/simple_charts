import {atom} from "jotai";
import {UserInfo} from "../models/ShareChartData";

export const userInfoAtom = atom<UserInfo | null>(null);

export const setUserInfoAtom = atom(null, async (get, set, userInfo: UserInfo) => {
    set(userInfoAtom, userInfo);
});
