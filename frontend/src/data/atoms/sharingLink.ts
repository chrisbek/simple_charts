import {atom} from "jotai";
import {sharingTokenAtom} from "./sharingToken";

export const sharingLinkAtom = atom<string | null>((get) => {
  const token = get(sharingTokenAtom);
  if (token === null) {
    return null;
  }

  return `${window.location.host}/share/chart/${token}`;
});
