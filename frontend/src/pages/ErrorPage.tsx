import {Box} from '@chakra-ui/react'

export const ErrorPage = () => {
  return (
      <Box bg='#FC8181' w="100vw" h="100vh" color='white' display='flex' alignItems='center' justifyContent='center'
           fontSize={'80'}>
        <div>An error occured</div>
      </Box>
  )
};
