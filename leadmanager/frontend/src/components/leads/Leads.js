import React, { useEffect, Fragment } from "react";
import { useDispatch, useSelector } from "react-redux";
import { getLeads, deleteLead } from "../../actions/leads";

function Leads(props) {
  // TODO: Prop types?
  const dispatch = useDispatch();

  useEffect(() => {
    dispatch(getLeads());
  }, []);

  const leads = useSelector((state) => state.leads.leads);

  return (
    <Fragment>
      <h2>Leads</h2>
      <table className="table table-striped">
        <thead>
          <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Email</th>
            <th>Message</th>
            <th></th>
          </tr>
        </thead>
        <tbody>
          {leads.map((lead) => (
            <tr key={lead.id}>
              <td>{lead.id}</td>
              <td>{lead.name}</td>
              <td>{lead.email}</td>
              <td>{lead.message}</td>
              <td>
                <button
                  onClick={() => dispatch(deleteLead(lead.id))}
                  className="btn btn-danger btn-sm"
                >
                  Delete
                </button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </Fragment>
  );
}

export default Leads;
