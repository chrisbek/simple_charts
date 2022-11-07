import {atom} from "jotai";
import {fetchSharingToken} from "../../api/sharing";
import {UserInfo} from "../models/ShareChartData";

export const sharingTokenAtom = atom<string | null>(null);
export const sharingTokenLoadingRequestedAtom = atom<boolean>(false);
export const sharingTokenLoadingAtom = atom<boolean>(false);

export const fetchSharingTokenAtom = atom(null, async (get, set, userInfo: UserInfo) => {
  set(sharingTokenLoadingAtom, true);
  set(sharingTokenLoadingRequestedAtom, false);
  const {token} = await fetchSharingToken(userInfo.email, userInfo.expirationDate);
  set(sharingTokenAtom, token);
  set(sharingTokenLoadingAtom, false);
});

export const setSharingTokenLoadingRequestedAtom = atom(null, async (get, set, value: boolean) => {
  set(sharingTokenLoadingRequestedAtom, value);
});
