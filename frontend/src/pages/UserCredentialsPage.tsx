import {useUserInfo} from "../data/hooks/useUserInfo";
import {useSharedChartDataLoading} from "../data/hooks/useSharedChartData";
import {SharedChartPage} from "./SharedChartPage";
import {useState} from "react";
import {
    FormControl,
    FormLabel,
    FormErrorMessage,
    Input,
    Box,
    Button,
} from '@chakra-ui/react'
import {UserInfo} from "../data/models/ShareChartData";

export const UserCredentialsPage = () => {
    const [sharedChartDataLoadingStarted, setSharedChartDataLoadingStarted] = useSharedChartDataLoading()
    const [, setUserInfo] = useUserInfo()

    async function onSubmit() {
        setUserInfo(new UserInfo(userEmail))
        setSharedChartDataLoadingStarted(true)
    }

    const [userEmail, setUserEmail] = useState('')
    const isError = userEmail === ''

    return (
        userEmail !== '' && sharedChartDataLoadingStarted ?
            <SharedChartPage/>
            :
            <Box minW="100%" minH="100%" display="flex" alignItems="center" justifyContent="center" pl="35%" pr="35%"
                 pt="15%">
                <FormControl isInvalid={isError}>
                    <FormLabel>Please enter your email in order to view the chart</FormLabel>
                    <Input type='email' value={userEmail} onChange={(e: any) => setUserEmail(e.target.value)}/>
                    {!isError ? (
                        undefined
                    ) : (
                        <FormErrorMessage>Email is required.</FormErrorMessage>
                    )}
                    <Button
                        mt={4}
                        colorScheme='teal'
                        type='submit'
                        disabled={(userEmail === '' || sharedChartDataLoadingStarted)}
                        onClick={onSubmit}
                    >
                        View Chart
                    </Button>
                </FormControl>
            </Box>
    )
};
