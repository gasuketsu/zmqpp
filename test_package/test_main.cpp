/*
 * This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/.
 *
 * This file is part of zmqpp.
 * Copyright (c) 2011-2017 Contributors as noted in the AUTHORS file.
 */

/*
 *  Created on: 24 June 2017
 *      Author: Tomoyuki Harada (@gasuketsu)
 */

#include "zmqpp/zmqpp.hpp"
#include <string>
#include <cassert>

int main()
{
    zmqpp::context ctx;
    zmqpp::socket req(ctx, zmqpp::socket_type::request);
    zmqpp::socket rep(ctx, zmqpp::socket_type::reply);

    rep.bind("inproc://test.sock");
    req.connect("inproc://test.sock");

    zmqpp::message req_msg;
    req_msg << "ping";
    req.send(req_msg);
    zmqpp::message received_msg;
    rep.receive(received_msg);
    assert(received_msg.get(0) == "ping");

    zmqpp::message rep_msg;
    rep_msg << "pong";
    rep.send(rep_msg);
    req.receive(received_msg);
    assert(received_msg.get(0) == "pong");

    return 0;
}
