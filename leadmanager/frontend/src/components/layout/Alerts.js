import React, { useEffect, Fragment, useRef } from "react";
import { withAlert } from "react-alert";
import { useSelector } from "react-redux";

function usePrevious(value) {
  const ref = useRef();
  useEffect(() => {
    ref.current = value;
  });
  return ref.current;
}

function Alerts(props) {
  // Define store states
  const error = useSelector((state) => state.errors);
  const message = useSelector((state) => state.messages);

  // previous states
  const prevState = {
    error: usePrevious(error),
    message: usePrevious(message),
  };

  // Define alert
  const alert = props.alert;

  // TODO: More efficient way?
  useEffect(() => {
    if (error != prevState.error) {
      try {
        if (error.msg.name) {
          alert.error(`Name: ${error.msg.name.join()}`);
        }
        if (error.msg.email) {
          alert.error(`Email: ${error.msg.email.join()}`);
        }
        if (error.msg.message) {
          alert.error(`Message: ${error.msg.message.join()}`);
        }
        if (error.msg.non_field_errors) {
          alert.error(error.msg.non_field_errors.join());
        }
        if (error.msg.username) {
          alert.error(error.msg.username.join());
        }
      } catch {}
    }

    if (message !== prevState.message) {
      if (message.deleteLead) {
        alert.success(message.deleteLead);
      }
      if (message.addLead) {
        alert.success(message.addLead);
      }
      if (message.passwordNotMatch) {
        alert.error(message.passwordNotMatch);
      }
    }
  }, [error, message]);

  return <Fragment></Fragment>;
}

export default withAlert()(Alerts);
