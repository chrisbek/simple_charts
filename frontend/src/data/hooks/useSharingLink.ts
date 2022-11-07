import {useAtom, useSetAtom} from "jotai";
import {sharingLinkAtom} from "../atoms/sharingLink";
import {setSharingTokenLoadingRequestedAtom, sharingTokenLoadingRequestedAtom} from "../atoms/sharingToken";

export const useSharingLink = () => {
  const [link] = useAtom(sharingLinkAtom);

  return link;
};


export const useSharingTokenLoadingRequested = (): [boolean, CallableFunction] => {
  const [sharingTokenInitializedRequested] = useAtom(sharingTokenLoadingRequestedAtom);
  const setSharingTokenInitializedRequested = useSetAtom(setSharingTokenLoadingRequestedAtom);

  return [sharingTokenInitializedRequested, setSharingTokenInitializedRequested];
}