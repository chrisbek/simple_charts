const getUtcFromDate = (date: Date): Date => {
    let date_utc = Date.UTC(date.getUTCFullYear(), date.getUTCMonth(),
        date.getUTCDate(), date.getUTCHours(),
        date.getUTCMinutes(), date.getUTCSeconds())
    return new Date(date_utc);
}

export const getUtcNow = (): Date => {
    return getUtcFromDate(new Date());
}