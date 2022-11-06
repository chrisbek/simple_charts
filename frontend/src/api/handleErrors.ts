export const handleErrors = async (response: Response) => {
  if (!response.ok) {
    const error = await response.json();
    throw Error(error?.detail?.[0]?.msg || "Unknown error");
  }
};
