import {useSharingLink, useSharingTokenLoadingRequested} from "../../data/hooks/useSharingLink";
import {SideMenu} from "./SideMenu";
import {CheckIcon, CopyIcon} from "@chakra-ui/icons";
import {
  Code,
  Heading,
  Link,
  FormControl,
  FormLabel,
  Input,
  Button,
  FormErrorMessage
} from '@chakra-ui/react'
import {useEffect, useState} from "react";
import {useFetchSharingLink} from "../../data/hooks/useFetchSharingLink";
import {useUserInfo} from "../../data/hooks/useUserInfo";
import {UserInfo} from "../../data/models/ShareChartData";
import {getUtcNow} from "../../utils/date";
import {dateIsValid, emailExists, emailExistsAndIsValid} from "../../utils/validators";

interface ShareMenuProps {
  show: boolean;
}


export const ShareMenu = ({show}: ShareMenuProps) => {
  const link = useSharingLink();
  const [copied, setCopied] = useState(false);
  const [, setSharingTokenLoadingRequested] = useSharingTokenLoadingRequested();
  const [userInfo, setUserInfo] = useUserInfo();
  const sharingTokenLoading = useFetchSharingLink();


  async function handleEmailInput(e: any) {
    let userEmail = e.target.value;
    setUserInfo((prevUserInfo: any) => {
      return new UserInfo(userEmail, prevUserInfo.expirationDate)
    })
  }

  async function handleExpirationDateInput(e: any) {
    let date = new Date(e.target.value);
    setUserInfo((prevUserInfo: any) => {
      return new UserInfo(prevUserInfo.email, date)
    })
  }

  async function onSubmit() {
    setSharingTokenLoadingRequested(true)
  }

  async function copyLink() {
    if (!link) return;

    try {
      await navigator.clipboard.writeText(link);
      setCopied(true);
    } catch (error) {
      console.error(error);
    }
  }

  useEffect(() => {
    setUserInfo(new UserInfo('', getUtcNow()))
  }, [])

  useEffect(() => {
    setCopied(false);
  }, [show]);


  let isError = true;
  return (
      <SideMenu show={show}>
        <Heading size="md" pb={3}>
          Create share link
        </Heading>
        <Heading size="xs" pb={3}>
          Please fill the following fields to create a sharable link:
        </Heading>
        <FormControl isRequired isInvalid={true}>
          <FormLabel>Email</FormLabel>
          <Input
              type='email'
              value={userInfo?.email}
              onChange={handleEmailInput}
          />
          {!emailExists(userInfo) ? <FormErrorMessage>Email is required.</FormErrorMessage> : undefined}
          {emailExists(userInfo) && !emailExistsAndIsValid(userInfo) ?
              <FormErrorMessage>Email is invalid.</FormErrorMessage> : undefined}

          <FormLabel>Expiration Date</FormLabel>
          <Input
              type="datetime-local"
              size="md"
              onChange={handleExpirationDateInput}
          />
          {!dateIsValid(userInfo) ? <FormErrorMessage>Expiration date is invalid.</FormErrorMessage> : undefined}

          <Button
              mt={4}
              colorScheme='teal'
              type='submit'
              disabled={sharingTokenLoading}
              onClick={onSubmit}
          >
            Create Link
          </Button>
        </FormControl>

        {link != null ? <Code
            p="8px"
            display="flex"
            flexDirection="column"
            alignItems="flex-end"
            cursor="pointer"
            onClick={copyLink}
        >
          <Link maxWidth="100%">{link}</Link>
          {copied ? <CheckIcon color="green"/> : <CopyIcon/>}
        </Code> : undefined}
      </SideMenu>
  );
};
