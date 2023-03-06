import React from 'react';
import { useModal } from '../../context/Modal';
import styled from 'styled-components';

function OpenModalButton({
  modalComponent, // component to render inside the modal
  buttonText, // text of the button that opens the modal
  onButtonClick, // optional: callback function that will be called once the button that opens the modal is clicked
  onModalClose // optional: callback function that will be called once the modal is closed
}) {
  const { setModalContent, setOnModalClose } = useModal();

  const onClick = () => {
    if (typeof onButtonClick === 'function') onButtonClick();
    if (typeof onModalClose === 'function') setOnModalClose(onModalClose);
    setModalContent(modalComponent);
  };

  return (
    <ModalButton as="button" onClick={onClick}>{buttonText}</ModalButton>
  );
}

const ModalButton = styled.button`
    box-sizing: border-box;
    display: flex;
    align-items: center;
    justify-content: center;
    width: 65px;
    height: 65px;
    border: 2px solid black;
    border-radius: 50px;
    margin: .3rem 1rem;
    background-color: rgba(30, 30, 30, 1);
    color: rgba(159, 159, 159, 1);
    font-size: 10pt;
`

export default OpenModalButton;
