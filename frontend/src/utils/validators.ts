import {UserInfo} from "../data/models/ShareChartData";

export const emailExistsAndIsValid = (userInfo: UserInfo | null): boolean => {
    if (userInfo instanceof UserInfo) {
        let re = /\S+@\S+\.\S+/;
        return re.test(userInfo.email);
    }

    return false
}

export const emailExists = (userInfo: UserInfo | null): boolean => {
    return userInfo instanceof UserInfo && userInfo.email !== ''
}

export const dateIsValid = (userInfo: UserInfo | null): boolean => {
    return userInfo?.expirationDate instanceof Date
}