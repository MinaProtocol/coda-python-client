import mock

from MinaClient import Client, Currency


@mock.patch("requests.post")
class TestMinaClient:
    """
    Tests the MinaClient.Client class
    """
    def _mock_response(
        self,
        status=200,
        content="CONTENT",
        json_data={"data": "{ foo: 'bar'}"},
        raise_for_status=None,
    ):

        mock_resp = mock.Mock()
        # mock raise_for_status call w/optional error
        mock_resp.raise_for_status = mock.Mock()

        if raise_for_status:
            mock_resp.raise_for_status.side_effect = raise_for_status
        # set status code and content
        mock_resp.status_code = status
        mock_resp.content = content
        # add json data if provided
        if json_data:
            mock_resp.json = mock.Mock(return_value=json_data)
        return mock_resp

    def test_get_daemon_status(self, mock_post, snapshot):
        mock_post.return_value = self._mock_response(json_data={"data": "foo"})

        client = Client()
        client.get_daemon_status()
        snapshot.assert_match(mock_post.call_args_list)

    def test_get_daemon_version(self, mock_post, snapshot):
        mock_post.return_value = self._mock_response(json_data={"data": "foo"})

        client = Client()
        client.get_daemon_version()
        snapshot.assert_match(mock_post.call_args_list)

    def test_get_wallets(self, mock_post, snapshot):
        mock_post.return_value = self._mock_response(json_data={"data": "foo"})

        client = Client()
        client.get_wallets()
        snapshot.assert_match(mock_post.call_args_list)

    def test_get_wallet(self, mock_post, snapshot):
        mock_post.return_value = self._mock_response(json_data={"data": "foo"})

        client = Client()
        client.get_wallet("pk")
        snapshot.assert_match(mock_post.call_args_list)

    def test_get_transaction_status(self, mock_post, snapshot):
        mock_post.return_value = self._mock_response(json_data={"data": "foo"})

        client = Client()
        client.get_transaction_status("payment_id")
        snapshot.assert_match(mock_post.call_args_list)

    def test_get_current_snark_worker(self, mock_post, snapshot):
        mock_post.return_value = self._mock_response(json_data={"data": "foo"})

        client = Client()
        client.get_current_snark_worker()
        snapshot.assert_match(mock_post.call_args_list)

    def test_get_sync_status(self, mock_post, snapshot):
        mock_post.return_value = self._mock_response(json_data={"data": "foo"})

        client = Client()
        client.get_sync_status()
        snapshot.assert_match(mock_post.call_args_list)

    def test_set_current_snark_worker(self, mock_post, snapshot):
        mock_post.return_value = self._mock_response(json_data={"data": "foo"})

        client = Client()
        client.set_current_snark_worker("pk", 1)
        snapshot.assert_match(mock_post.call_args_list)

    def test_create_wallet(self, mock_post, snapshot):
        mock_post.return_value = self._mock_response(json_data={"data": "foo"})

        client = Client()
        client.create_wallet("password")
        snapshot.assert_match(mock_post.call_args_list)

    def test_send_payment(self, mock_post, snapshot):
        mock_post.return_value = self._mock_response(json_data={"data": "foo"})

        client = Client()
        currency = Currency(1)
        fee = Currency(0.1)
        client.send_payment("to_pk", "from_pk", currency, fee, "memo")
        snapshot.assert_match(mock_post.call_args_list)

    def test_get_best_chain(self, mock_post, snapshot):
        mock_post.return_value = self._mock_response(json_data={"data": "foo"})

        client = Client()
        max_length = 42
        client.get_best_chain(max_length=max_length)
        snapshot.assert_match(mock_post.call_args_list)

    def test_get_block_by_height(self, mock_post, snapshot):
        mock_post.return_value = self._mock_response(json_data={"data": "foo"})

        client = Client()
        height = 42
        client.get_block_by_height(height=height)
        snapshot.assert_match(mock_post.call_args_list)

    def test_get_block_by_state_hash(self, mock_post, snapshot):
        mock_post.return_value = self._mock_response(json_data={"data": "foo"})

        client = Client()
        state_hash = "some_state_hash"
        client.get_block_by_state_hash(state_hash=state_hash)
        snapshot.assert_match(mock_post.call_args_list)
