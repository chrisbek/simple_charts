import {API_URL} from "../constants/api";
import {ChartData} from "../data/models/ChartData";
import {handleErrors} from "./handleErrors";

export const fetchSharingToken = async (
    email: string,
    expirationDate: Date | null
): Promise<{ token: string }> => {

  const response = await fetch(`${API_URL}/share`, {
    method: 'POST',
    headers: {"content-type": "application/json"},
    body: JSON.stringify({
      email: email,
      expiration_date: expirationDate?.toISOString().slice(0, -1)
    })
  });
  await handleErrors(response);

  return await response.json();
};

export const fetchSharedChartData = async (
    token: string,
    email: string
): Promise<ChartData> => {
  const response = await fetch(`${API_URL}/chart/shared/${token}/${email}`, {
    headers: {"content-type": "application/json"},
  });
  await handleErrors(response);

  return await response.json();
};
